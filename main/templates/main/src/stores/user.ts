import {type Ref, ref} from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const id: Ref<number> = ref(0);
  const type: Ref<string> = ref('');

  async function login(){
      let res = await axios.get(window.origin + '/api/auth');

      if(res.data['result']){
        id.value = Number(res.data['id']);
        type.value = String(res.data['type']);
      }
  }
  function logout(){
    axios.post(window.origin + '/api/logout',{}, {headers: {"X-CSRFToken": getCookie('csrftoken')}}).then(res => {
      id.value = 0;
      type.value = '';
    });
  }
  login();

  function getCookie(cname: string) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

  return { id, type, login, logout, getCookie };
})

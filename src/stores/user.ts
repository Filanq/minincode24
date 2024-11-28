import {type Ref, ref} from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const id: Ref<number> = ref(0);
  const type: Ref<string> = ref('');

  function login(){
    axios.get(window.origin + '/api/auth/').then(res => {
      if(res.data['result']){
        id.value = Number(res.data['id']);
        type.value = String(res.data['type']);
      }
    });
  }
  function logout(){
    axios.post(window.origin + '/api/logout/').then(res => {
      id.value = 0;
      type.value = '';
    });
  }

  return { id, type, login, logout };
})

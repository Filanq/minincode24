import {Ref, ref} from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  const id: Ref<number> = ref(0);

  return { id }
})

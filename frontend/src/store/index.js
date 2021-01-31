import Vue from 'vue'
import Vuex from 'vuex'

import AnounceModule from './anounce'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    anounce: AnounceModule
  }
})

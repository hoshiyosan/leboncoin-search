import http from '@/plugins/http'

export default {
    namespaced: true,
    state: {
        anounces: []
    },
    getters: {
        anouncesInbox(state) {
            return state.anounces.filter(anounce => anounce.decision === 'inbox')
        },
        anouncesFavorites(state) {
            return state.anounces.filter(anounce => anounce.decision === 'favorite')
        },
        anouncesBlacklist(state) {
            return state.anounces.filter(anounce => anounce.decision === 'blacklist')
        },
        anounces(state) {
            return state.anounces
        }
    },
    mutations: {
        setAnounces(state, anounces) {
            state.anounces = anounces;
        },
        setAnounceDecision(state, { anounceUid, decision }) {
            for (let anounce of state.anounces) {
                if (anounce.uid === anounceUid) {
                    anounce.decision = decision;
                }
            }
        }
    },
    actions: {
        updateAnounces({ commit }) {
            http.get('/anounces')
                .then(response => {
                    const anounces = response.data;
                    commit("setAnounces", anounces);
                })
        },
        inboxAnounce({ commit }, anounceUid) {
            http.post(`/anounces/inbox/${anounceUid}`)
                .then(() => {
                    commit("setAnounceDecision", { anounceUid: anounceUid, decision: "inbox" })
                })
        },
        favoriteAnounce({ commit }, anounceUid) {
            http.post(`/anounces/favorites/${anounceUid}`)
                .then(() => {
                    commit("setAnounceDecision", { anounceUid: anounceUid, decision: "favorite" })
                })
        },
        blacklistAnounce({ commit }, anounceUid) {
            http.post(`/anounces/blacklist/${anounceUid}`)
                .then(() => {
                    commit("setAnounceDecision", { anounceUid: anounceUid, decision: "blacklist" })
                })
        }
    }
}

import { writable } from 'svelte/store';
import { supabase } from '../lib/supabaseClient';

const bidsChanges = supabase
	.channel('custom-all-channel')
	.on('postgres_changes', { event: '*', schema: 'public', table: 'bids' }, (payload) => {
		//console.log('Change received in store!', payload);
		bidsStore.set(payload);
	})
	.subscribe();

function createBidsStore() {
	const { subscribe, set, update } = writable([]);

	return {
		subscribe,
		set,
		update
	};
}

export const bidsStore = createBidsStore();

// subscribe to changes in the `bidsStore` store
bidsStore.subscribe((value) => {
	console.log('bidsStore changed:', value);
});

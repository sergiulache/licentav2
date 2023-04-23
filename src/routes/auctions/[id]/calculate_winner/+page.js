//import { page } from '@sveltejs/kit';
import { supabase } from '$lib/supabaseClient';

export async function load(page) {
	// save the item_id from the url
	const item_id = page.params.id;

	// select all bids from bids table where item_id = item_id and data from users table where user_id = bidder_id
	const { data: bids, error } = await supabase.rpc('get_bids_with_users', { p_item_id: item_id });

	console.log('bids', bids);
	console.log('error', error);

	console.log('calculating winner');

	return {
		data: bids
	};
}

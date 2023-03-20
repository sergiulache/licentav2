import { error } from '@sveltejs/kit';
import { supabase } from '$lib/supabaseClient';
import { getCurrentUserID, isAuthenticated } from '$lib/auth';
import { goto } from '$app/navigation';
import { redirect } from '@sveltejs/kit';
import { userSession } from '../../../stores/userSession';
import { get } from 'svelte/store';
import { browser } from '$app/environment';

//export const ssr = false;

async function verifyId(id) {
	const { data } = await supabase.from('items').select();
	const ids = data.map((item) => item.item_id);

	if (ids.includes(id)) {
		console.log('id is valid');
		return true;
	}
	console.log('id is invalid');
	return false;
}

export async function load({ params }) {
	let validId = await verifyId(params.id);
	console.log(validId);
	let userID;
	if (browser) {
		userID = await getCurrentUserID();
		//console.log(userID);
	}

	// select all items where poster_Id = userID
	const { data, error } = await supabase.from('items').select().eq('poster_id', userID);

	// filter so that only the items with the id = params.id are left
	const filteredData = data.filter((item) => item.item_id == params.id);
	console.log('filteredData         ' + filteredData);

	// return the filtered data
	if (validId) {
		return {
			items: filteredData ?? []
		};
	}
}

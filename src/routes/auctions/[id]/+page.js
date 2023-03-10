import { error } from '@sveltejs/kit';
import { supabase } from '$lib/supabaseClient';
import { getCurrentUserID, isAuthenticated } from '$lib/auth';
import { goto } from '$app/navigation';
import { redirect } from '@sveltejs/kit';

//export const ssr = false;

async function verifyId(id) {
	const { data } = await supabase.from('items').select();
	const ids = data.map((item) => item.id);
	//console.log(ids);

	if (ids.includes(parseInt(id))) {
		return true;
	}
	return false;
}

export async function load({ params }) {
	let loggedIn = await isAuthenticated();
	if (!loggedIn) {
		throw redirect(302, '/auth/login');
	}
	let validId = await verifyId(params.id);
	//console.log(validId);

	const userID = await getCurrentUserID();
	console.log(userID);

	// select all items where poster_Id = userID
	const { data, error } = await supabase.from('items').select().eq('poster_Id', userID);

	console.log(data);

	// filter so that only the items with the id = params.id are left
	const filteredData = data.filter((item) => item.id == params.id);
	console.log(filteredData);

	// return the filtered data
	if (validId) {
		return {
			items: filteredData ?? []
		};
	}

	throw error(404, 'Not found');
}

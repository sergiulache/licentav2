import { supabase } from '$lib/supabaseClient';
import { redirect } from '@sveltejs/kit';
import { isAuthenticated } from '$lib/auth';
import { userSession } from '../../stores/userSession';
import { getCurrentUserID } from '$lib/auth';
import { get } from 'svelte/store';

export async function load() {
	const { data } = await supabase.from('items').select();

	const userID = await getCurrentUserID();
	console.log('userID in my auctions' + userID);
	// select all items where poster_Id = userID
	const { data: userItems, error } = await supabase.from('items').select().eq('poster_id', userID);

	return {
		data: userItems ?? []
	};
}

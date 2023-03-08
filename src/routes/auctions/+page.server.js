import { supabase } from '$lib/supabaseClient';
import { isAuthenticated } from '../../lib/auth';
import { redirect } from '@sveltejs/kit';

export async function load() {
	console.log('loading auctions');
	if (!isAuthenticated()) {
		// redirect to login
		console.log('redirecting to login');
		throw redirect(307, '/auth/login');
	}

	const { data } = await supabase.from('items').select();
	console.log('loaded auctions server');
	return {
		items: data ?? []
	};
}

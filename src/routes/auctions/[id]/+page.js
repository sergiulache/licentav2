import { error } from '@sveltejs/kit';
import { supabase } from '$lib/supabaseClient';

async function verifyId(id) {
	const { data } = await supabase.from('items').select();
	const ids = data.map((item) => item.id);
	console.log(ids);
	if (ids.includes(parseInt(id))) {
		return true;
	}
	return false;
}

export async function load({ params }) {
	let validId = await verifyId(params.id);
	console.log(params);
	console.log(validId);
	if (validId) {
		return {
			title: 'Hello world!',
			content: 'Welcome to our blog. Lorem ipsum dolor sit amet...'
		};
	}

	throw error(404, 'Not found');
}

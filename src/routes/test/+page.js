import { supabase } from '$lib/supabaseClient';
import { redirect } from '@sveltejs/kit';
import { isAuthenticated } from '$lib/auth';
import { userSession } from '../../stores/userSession';
import { getCurrentUserID } from '$lib/auth';
import { get } from 'svelte/store';

export async function load() {
	// select auction data from supabase where item_id = 0de4fb43-0915-4113-8ab0-bbdf3dc4a7a9
	const { data, error } = await supabase
		.from('items')
		.select()
		.eq('item_id', '0de4fb43-0915-4113-8ab0-bbdf3dc4a7a9');

	// select all bids from bids table where item_id = data[0].item_id
	const { data: bids } = await supabase.from('bids').select().eq('item_id', data[0].item_id);

	// select everything from the reviews table where reviewed_id = poster_id from the items table
	const { data: reviews } = await supabase
		.from('reviews')
		.select()
		.eq('reviewed_id', data[0].poster_id);

	// select ALL first_name from users table where user_id = reviewer_id from reviews table
	const { data: reviewerNames } = await supabase
		.from('users')
		.select('first_name')
		.in(
			'user_id',
			reviews.map((review) => review.reviewer_id)
		);

	//console.log('reviewerNames', reviewerNames);

	// add reviewerNames to reviews

	reviews.forEach((review, index) => {
		//console.log('index', index);
		review.reviewer_name = reviewerNames[index].first_name;
	});

	//console.log('reviews', reviews);

	// return data[0] and sellerReviews
	return { props: { data: data[0], sellerReviews: reviews, bids } };
}

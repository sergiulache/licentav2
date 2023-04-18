import { supabase } from '$lib/supabaseClient';
import { browser } from '$app/environment';
import { goto } from '$app/navigation';

export async function load({ params }) {
	// select auction data from supabase where item_id = 0de4fb43-0915-4113-8ab0-bbdf3dc4a7a9
	console.log('current item id', params.id);
	const { data, error } = await supabase.from('items').select().eq('item_id', params.id);

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

	// select expiration date from items table wher item_id is the same as the item_id from the bids table
	const { data: expirationDate } = await supabase
		.from('items')
		.select('expiration_date')
		.eq('item_id', data[0].item_id);

	reviews.forEach((review, index) => {
		//console.log('index', index);
		review.reviewer_name = reviewerNames[index].first_name;
	});

	if (browser) {
		$: {
			goto(`/auctions/${params.id}`);
		}
	}

	// return data[0] and sellerReviews
	return { props: { data: data[0], sellerReviews: reviews, bids, expirationDate: expirationDate } };
}

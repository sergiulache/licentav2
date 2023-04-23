import { supabase } from '$lib/supabaseClient';
import { browser } from '$app/environment';
import { goto } from '$app/navigation';

export async function load({ params }) {
	console.log('current item id', params.id);

	const { data, error } = await supabase.rpc('get_auction_data', { p_item_id: params.id });

	console.log('error', error);

	const itemData = data[0].item_data;
	const bids = data.map((row) => row.bid_data).filter((bid) => bid !== null);
	const reviews = data
		.map((row) => ({ ...row.review_data, reviewer_name: row.reviewer_name }))
		.filter((review) => review.review_id !== null);
	const expirationDate = data[0].expiration_date;

	if (browser) {
		$: {
			goto(`/auctions/${params.id}`);
		}
	}

	return { props: { data: itemData, sellerReviews: reviews, bids, expirationDate } };
}

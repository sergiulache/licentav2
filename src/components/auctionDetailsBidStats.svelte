<script>
	import { bidsStore } from '../stores/bidsStore';
	import { supabase } from '$lib/supabaseClient';
	import { userSession } from '../stores/userSession';
	import { browser } from '$app/environment';
	export let data;

	let currentHighestBidderId = 0;
	let highestBid = 100000;
	let highestBidItemId = 0;

	console.log('data in auctionDetailsBidStats.svelte: ', JSON.stringify(data.props.bids));
	let bidCount = 0;
	if (
		data.props.bids &&
		data.props.bids != null &&
		data.props.bids != undefined &&
		data.props.bids.length > 0
	) {
		bidCount = data.props.bids[0].length;

		// for each bid in data.props.bids
		data.props.bids[0].forEach((bid) => {
			// if bid.amount > highestBid
			//console.log('bid.bid_amount: ', bid.bid.bid_amount);
			if (bid.bid.bid_amount < highestBid) {
				// set highestBid to bid.amount
				highestBid = bid.bid.bid_amount;
			}
		});
	}

	// modify current bid in Items to be highestBid
	async function modifyHighestBidInItemsTable(highestBid, item_id) {
		const { dataNewBid, error } = await supabase
			.from('items')
			.update({ current_bid: highestBid })
			.eq('item_id', item_id)
			.single();
	}

	async function modifyCurrentBidHolderInItemsTable(user_id, item_id) {
		const { dataNewBidder, error } = await supabase
			.from('items')
			.update({ bid_holder: user_id })
			.eq('item_id', item_id)
			.single();
	}

	let bidChanges = $bidsStore;
	bidsStore.subscribe((value) => {
		bidChanges = value;
		if (bidChanges && bidChanges.new && bidChanges.new.bid_amount < highestBid) {
			highestBid = bidChanges.new.bid_amount;
			currentHighestBidderId = bidChanges.new.bidder_id;
			highestBidItemId = bidChanges.new.item_id;
			modifyHighestBidInItemsTable(highestBid, highestBidItemId);
			modifyCurrentBidHolderInItemsTable(currentHighestBidderId, highestBidItemId);
			bidCount += 1;
		}
	});
</script>

<div>
	<dl class="mt-5 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-2">
		<div class="relative bg-white pt-5 px-4 sm:pt-6 sm:px-6 shadow rounded-lg overflow-hidden">
			<dt>
				<div class="absolute bg-indigo-500 rounded-md p-3">
					<!-- Heroicon name: outline/users -->
					<i class="fa-solid fa-users-between-lines fa-lg text-white" />
				</div>
				<p class="ml-16 text-sm font-medium text-gray-500 truncate">Total Bids</p>
			</dt>
			<dd class="ml-14 pb-6 flex flex-col items-baseline sm:pb-7">
				<p class="text-xl font-semibold text-gray-900">{bidCount}</p>
				<p class="ml-2 flex text-sm font-semibold text-green-600 pt-1">
					<!-- Heroicon name: solid/arrow-sm-up -->
					<i class="fa-solid fa-arrow-up text-green-500 pr-1" />
					<span class="sr-only"> Increased by </span>
					2
				</p>
			</dd>
		</div>

		<div class="relative bg-white pt-5 px-4 sm:pt-6 sm:px-6 shadow rounded-lg overflow-hidden">
			<dt>
				<div class="absolute bg-indigo-500 rounded-md p-3">
					<!-- Heroicon name: outline/mail-open -->
					<i class="fa-solid fa-dollar-sign text-white fa-lg mx-1.5" />
				</div>
				<p class="ml-16 text-sm font-medium text-gray-500 truncate">Current Bid</p>
			</dt>
			{#if highestBid !== 100000}
				<dd class="ml-14 pb-6 flex flex-col items-baseline sm:pb-7">
					<p class="text-xl font-semibold text-gray-900">
						$ {highestBid.toLocaleString('en-US', {
							style: 'decimal',
							minimumFractionDigits: 2,
							maximumFractionDigits: 2
						})}
					</p>
					<p class="ml-2 flex items-baseline text-sm font-semibold text-green-600 pt-1">
						<i class="fa-solid fa-arrow-up text-green-500 pr-1" />
						<span class="sr-only"> Increased by </span>
						5.4%
					</p>
				</dd>
			{:else}
				<dd class="ml-14 pb-6 flex flex-col items-baseline sm:pb-7">
					<p class="text-xl font-semibold text-gray-900">No bids yet</p>
				</dd>
			{/if}
		</div>
	</dl>
</div>

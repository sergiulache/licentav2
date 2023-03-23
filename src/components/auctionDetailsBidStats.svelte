<script>
	export let data;

	//console.log('data in auctionDetailsBidStats.svelte: ', JSON.stringify(data.props.bids));

	let bidCount = data.props.bids.length;
	let highestBid = 0;
	// for each bid in data.props.bids
	data.props.bids.forEach((bid) => {
		// if bid.amount > highestBid
		if (bid.bid_amount > highestBid) {
			// set highestBid to bid.amount
			highestBid = bid.bid_amount;
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
		</div>
	</dl>
</div>

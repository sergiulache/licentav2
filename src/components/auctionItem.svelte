<script>
	export let data;
</script>

<li>
	<a href="/auctions/{data.item_id}" class="block hover:bg-gray-50">
		<div class="px-4 py-4 flex items-center sm:px-6">
			<div class="min-w-0 flex-1 sm:flex sm:items-center sm:justify-between">
				<div class="truncate">
					<div class="flex text-sm">
						<p class="font-medium text-indigo-600 truncate">{data.title}</p>
					</div>
					<div class="mt-2 flex">
						<div class="flex items-center text-sm text-gray-500">
							<!-- Heroicon name: solid/calendar -->
							<i class="fa-solid fa-calendar-days fa-lg pr-2 text-gray-400 " />
							<p>
								Closing on
								<time datetime="2020-01-07">{data.expiration_date}</time>
							</p>
						</div>
					</div>
					<div class="mt-2 flex">
						<div class="flex items-center text-sm text-gray-500">
							<!-- Heroicon name: solid/calendar -->
							<i class="fa-solid fa-dollar-sign fa-lg pr-1  h-5 w-5 text-gray-400" />
							{#if data.current_bid == null}
								<p>
									Current bid: <span class="font-medium text-indigo-500">No bids yet</span>
								</p>
							{:else}
								<p>
									Current bid: <span class="font-medium text-indigo-500"
										>${data.current_bid.toLocaleString('en-US', {
											style: 'decimal',
											minimumFractionDigits: 2,
											maximumFractionDigits: 2
										})}</span
									>
								</p>
							{/if}
						</div>
					</div>
				</div>
			</div>
			<div class="ml-5 flex-shrink-0">
				{#if new Date(data.expiration_date) < new Date()}
					<span
						class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800"
					>
						Closed
					</span>
				{:else}
					<span
						class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800"
					>
						Active
					</span>
				{/if}
				<i class="fa-solid fa-caret-right fa-lg text-gray-400" />
			</div>
		</div>
	</a>
</li>

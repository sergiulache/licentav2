<script>
	export let data;

	console.log({
		'expiration date: ': new Date(data.expiration_date),
		'current date: ': new Date(),
		'is expired: ': new Date(data.expiration_date) < new Date()
	});
</script>

<tr>
	<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
		>{data.title}</td
	>
	{#if new Date(data.expiration_date) < new Date()}
		<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
			><span class="inline-flex rounded-full bg-green-100 px-2 leading-5 text-green-800"
				>Auction closed</span
			></td
		>
	{:else if data.current_bid == null}
		<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
			><span class="inline-flex rounded-full bg-red-100 px-2  leading-5 text-red-600"
				>No bids yet</span
			></td
		>
	{:else if data.current_bid !== null && new Date(data.expiration_date) > new Date()}
		<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
			><span class="inline-flex rounded-full bg-yellow-100 px-2  leading-5 text-yellow-600"
				>Ongoing</span
			></td
		>
	{:else}
		<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
			><span class="inline-flex rounded-full bg-green-100 px-2 leading-5 text-green-800"
				>Auction closed</span
			></td
		>
	{/if}
	{#if data.current_bid == null}
		<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
			><span class="inline-flex rounded-full bg-red-100 px-2  leading-5 text-red-600"
				>No bids yet</span
			></td
		>
	{:else}
		<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">
			<i
				class="fa-solid fa-dollar-sign fa-lg pr-1  h-5 w-5 text-gray-400"
			/>{data.current_bid.toLocaleString('en-US', {
				style: 'decimal',
				minimumFractionDigits: 2,
				maximumFractionDigits: 2
			})}
		</td>
	{/if}

	<td class="hidden whitespace-nowrap px-3 py-4 text-sm text-gray-500 lg:table-cell"
		><i class="fa-solid fa-calendar-days fa-lg pr-2 text-gray-400 " />{data.expiration_date}</td
	>
	<td class="whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6">
		<a href="/auctions/{data.item_id}" class="text-indigo-600 hover:text-indigo-900"
			>View<span class="sr-only">, Lindsay Walton</span></a
		>
	</td>
</tr>

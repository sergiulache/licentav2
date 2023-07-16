<script>
	export let data;
</script>

<tr>
	<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">
		<i
			class="fa-solid fa-dollar-sign fa-lg pr-1  h-5 w-5 text-gray-400"
		/>{data.bid_amount.toLocaleString('en-US', {
			style: 'decimal',
			minimumFractionDigits: 2,
			maximumFractionDigits: 2
		})}
	</td>
	<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
		>{data.bidder_id}</td
	>
	<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
		>{data.buyer_rating}</td
	>
	<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
		>{data.bid_completion_time}</td
	>
	<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
		>{data.past_jobs}</td
	>
	<td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6"
		>{data.city}, {data.country}</td
	>
</tr>

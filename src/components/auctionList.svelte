<script>
	import AuctionItem from './auctionItem.svelte';

	export let data;

	// console log jsonified data
	//console.log(JSON.stringify(data));
</script>

<div class="bg-white shadow overflow-hidden sm:rounded-md p-4 sm:ml-64">
	<ul class="divide-y divide-gray-200">
		{#each data.data as auction}
			<li>
				<AuctionItem data={auction} />
			</li>
		{/each}
	</ul>
</div>

<script>
	import AuctionItem from './auctionItem.svelte';
	import Autocomplete from '@smui-extra/autocomplete';
	import { onMount } from 'svelte';

	export let data;

	let auctionNames = [];
	let selectedAuction = '';
	let isLoading = true; // for the loading spinner

	onMount(() => {
		data.data.forEach((item) => {
			auctionNames.push(item.title);
		});
		isLoading = false; // once the data has been loaded, set this to false
	});

	$: filteredAuctions = selectedAuction
		? data.data.filter((auction) => auction.title === selectedAuction)
		: data.data;

	$: autoCompleteOptions = selectedAuction
		? auctionNames
				.filter((name) => name.toLowerCase().includes(selectedAuction.toLowerCase()))
				.slice(0, 5)
		: auctionNames;
</script>

<div class="bg-white shadow overflow-hidden sm:rounded-md p-4 sm:ml-64">
	<div class="columns margins">
		<div>
			{#if isLoading}
				<div style="display: flex; justify-content: center">
					<div class="loader" />
				</div>
			{:else}
				<Autocomplete
					options={autoCompleteOptions}
					bind:value={selectedAuction}
					label="Search Auctions"
				/>
			{/if}
		</div>
	</div>
	<ul class="divide-y divide-gray-200">
		{#each filteredAuctions as auction}
			<li>
				<AuctionItem data={auction} />
			</li>
		{/each}
	</ul>
</div>

<style>
	.loader {
		border: 16px solid #f3f3f3; /* Light grey */
		border-top: 16px solid #3498db; /* Blue */
		border-radius: 50%;
		width: 60px;
		height: 60px;
		animation: spin 2s linear infinite;
	}

	@keyframes spin {
		0% {
			transform: rotate(0deg);
		}
		100% {
			transform: rotate(360deg);
		}
	}
</style>

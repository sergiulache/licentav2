<script>
	import AuctionItem from './auctionItem.svelte';
	import { onMount } from 'svelte';

	export let data;

	let auctionNames = [];
	let searchQuery = '';
	let isLoading = true; // for the loading spinner
	let currentPage = 1; // track the current page
	const itemsPerPage = 7; // how many items to display per page

	onMount(() => {
		data.data.forEach((item) => {
			auctionNames.push(item.title);
		});
		isLoading = false; // once the data has been loaded, set this to false
	});

	let filteredAuctions = data.data;
	function search() {
		filteredAuctions = data.data.filter((auction) =>
			auction.title.toLowerCase().includes(searchQuery.toLowerCase())
		);
	}

	$: totalPages = Math.ceil(filteredAuctions.length / itemsPerPage); // calculate total pages
	$: paginatedAuctions = filteredAuctions.slice(
		(currentPage - 1) * itemsPerPage,
		currentPage * itemsPerPage
	); // display only items for current page
	$: pageNumbers = Array.from({ length: totalPages }, (_, i) => i + 1); // create array of page numbers
</script>

<div class="bg-white shadow overflow-hidden sm:rounded-md p-4 sm:ml-64">
	<div class="columns margins">
		<div class="autocomplete-container">
			{#if isLoading}
				<div style="display: flex; justify-content: center">
					<div class="loader" />
				</div>
			{:else}
				<div>
					<label for="search" class="block text-sm font-medium text-gray-700">Search Auctions</label
					>
					<div class="mt-1 relative rounded-md shadow-sm">
						<input
							bind:value={searchQuery}
							type="text"
							name="search"
							id="search"
							class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pr-12 sm:text-sm border-gray-300 rounded-md"
							placeholder="Search..."
						/>
						<button
							on:click={search}
							class="absolute inset-y-0 right-0 px-3 flex items-center bg-indigo-500 text-white rounded-r-md cursor-pointer"
						>
							Search
						</button>
					</div>
				</div>
			{/if}
		</div>
	</div>
	<ul class="divide-y divide-gray-200">
		{#each paginatedAuctions as auction}
			<li>
				<AuctionItem data={auction} />
			</li>
		{/each}
	</ul>
	<div class="flex justify-center my-4">
		<button
			on:click={() => (currentPage = currentPage > 1 ? currentPage - 1 : 1)}
			class="mx-2 bg-indigo-500 text-white px-4 py-2 rounded-md"
		>
			Previous
		</button>
		{#each pageNumbers as page}
			<button
				on:click={() => (currentPage = page)}
				class="mx-2 px-4 py-2 rounded-md text-white {currentPage === page
					? 'bg-indigo-700'
					: 'bg-indigo-500'}"
			>
				{page}
			</button>
		{/each}
		<button
			on:click={() => (currentPage = currentPage < totalPages ? currentPage + 1 : totalPages)}
			class="mx-2 bg-indigo-500 text-white px-4 py-2 rounded-md"
		>
			Next
		</button>
	</div>
</div>

<style>
	.loader {
		border: 16px solid #f3f3f3; /* Light grey */
		border-top: 16px solid #3498db; /* Blue */
		border-radius: 50%;
		width: 120px;
		height: 120px;
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

	.autocomplete-container {
		width: 50%;
		margin: auto;
		margin-bottom: 1em;
		padding: 0.5em;
		border-radius: 5px;
		max-height: 12px;
	}

	.autocomplete {
		width: 100%;
	}
</style>

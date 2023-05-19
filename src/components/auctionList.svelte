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

	$: displayedPageNumbers = pageNumbers.reduce((acc, page) => {
		if (page === 1 || page === totalPages || (page >= currentPage - 2 && page <= currentPage + 2)) {
			acc.push(page);
		} else if (page === currentPage - 3 || page === currentPage + 3) {
			acc.push('...');
		}
		return acc;
	}, []);
</script>

<div class="bg-white shadow overflow-hidden sm:rounded-md p-4 sm:ml-64">
	<div class="columns margins">
		<div class="mt-1 relative rounded-md shadow-sm">
			{#if isLoading}
				<div style="display: flex; justify-content: center">
					<div class="loader" />
				</div>
			{:else}
				<div class="absolute inset-y-0 left-0 pl-2 flex items-center pointer-events-none">
					<span class="text-gray-500 sm:text-sm"> 🔍 </span>
				</div>
				<input
					bind:value={searchQuery}
					type="text"
					class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pl-7 pr-12 sm:text-sm border-gray-300 rounded-md"
					placeholder="Search Auctions"
				/>
				<button
					on:click={search}
					class="absolute inset-y-0 right-0 px-3 flex items-center bg-indigo-500 text-white rounded-r-md"
					>Search</button
				>
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
	<nav
		class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6"
		aria-label="Pagination"
	>
		<div class="flex-1 flex justify-between sm:hidden">
			{#if currentPage !== 1}
				<button
					on:click={() => currentPage--}
					class="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 hover:text-gray-500"
				>
					Previous
				</button>
			{/if}
			{#if currentPage !== totalPages}
				<button
					on:click={() => currentPage++}
					class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
				>
					Next
				</button>
			{/if}
		</div>
		<div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
			<div>
				<p class="text-sm text-gray-700">
					<span class="font-medium">{(currentPage - 1) * itemsPerPage + 1}</span>
					<span class="font-medium">-</span>
					<span class="font-medium">{currentPage * itemsPerPage}</span>
					<span>of</span>
					<span class="font-medium">{filteredAuctions.length}</span>
					<span>results</span>
				</p>
			</div>
			<div>
				<nav
					class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px"
					aria-label="Pagination"
				>
					{#each displayedPageNumbers as page}
						{#if page === '...'}
							<span
								class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50"
							>
								...
							</span>
						{:else}
							<button
								class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-blue-100 {currentPage ===
								page
									? 'bg-green-200'
									: ''}"
								on:click={() => (currentPage = page)}
							>
								{page}
							</button>
						{/if}
					{/each}
				</nav>
			</div>
		</div>
	</nav>
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

<!-- This example requires Tailwind CSS v2.0+ -->
<script>
	import { goto } from '$app/navigation';
	import UserAuctionsItem from './userAuctionsItem.svelte';

	function handleNewAuction() {
		goto('/auctions/new');
	}

	export let data;
</script>

<div class="px-4 sm:px-6 lg:px-8 p-4 sm:ml-64">
	<div class="sm:flex sm:items-center">
		<div class="sm:flex-auto">
			<h1 class="text-xl font-semibold text-gray-900">My auctions</h1>
			<p class="mt-2 text-sm text-gray-700">
				A list of all the auctions you have created, their current status and the highest bid.
			</p>
		</div>
		<div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
			<button
				on:click={handleNewAuction}
				type="button"
				class="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto"
				>Add auction</button
			>
		</div>
	</div>
	<div
		class="-mx-4 mt-8 overflow-hidden shadow ring-1 ring-black ring-opacity-5 sm:-mx-6 md:mx-0 md:rounded-lg"
	>
		<table class="min-w-full divide-y divide-gray-300">
			<thead class="bg-gray-50">
				<tr>
					<th
						scope="col"
						class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">Title</th
					>
					<th scope="col" class="py-3.5 px-3 text-left text-sm font-semibold text-gray-900 sm:pl-7"
						>Status</th
					>
					<th class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6"
						>Current bid</th
					>
					<th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
						>Expiration date</th
					>
					<th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6">
						<span class="sr-only">View</span>
					</th>
				</tr>
			</thead>
			<tbody class="divide-y divide-gray-200 bg-white">
				{#each data.data as auction}
					<UserAuctionsItem data={auction} />
				{/each}

				<!-- More people... -->
			</tbody>
		</table>
	</div>
</div>

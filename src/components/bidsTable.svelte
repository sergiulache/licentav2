<!-- This example requires Tailwind CSS v2.0+ -->
<script>
	import { goto } from '$app/navigation';
	import BidsTableSingleItem from './bidsTableSingleItem.svelte';
	import UserAuctionsItem from './userAuctionsItem.svelte';
	export let data;

	console.log(data);

	function handleCalculateWinner() {
		// get the current URL pathname
		let path = window.location.pathname;

		// split the path by slashes and remove the last segment ('view_bids')
		let pathSegments = path.split('/');
		pathSegments.pop();

		// add 'calculate_winner' to the path segments and join them with slashes
		pathSegments.push('calculate_winner');
		let newPath = pathSegments.join('/');

		// navigate to the new path
		goto(newPath);
	}
</script>

<div class="px-4 sm:px-6 lg:px-8 p-4 sm:ml-64">
	<div class="sm:flex sm:items-center">
		<div class="sm:flex-auto">
			<h1 class="text-xl font-semibold text-gray-900">Current bids</h1>
			<p class="mt-2 text-sm text-gray-700">A list of all of the bids for the current auction.</p>
		</div>
		<div class="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
			<button
				on:click={handleCalculateWinner}
				type="button"
				class="inline-flex items-center justify-center rounded-md border border-transparent bg-green-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto"
				>Calculate winner</button
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
						class="py-3.5 pl-4 px-3 text-left text-sm font-semibold text-gray-900 sm:pl-6"
						>Bid amount</th
					>
					<th scope="col" class="py-3.5 px-3 text-left text-sm font-semibold text-gray-900 sm:pl-7"
						>Bidder UID</th
					>
					<th class="py-3.5 px-3 text-left text-sm font-semibold text-gray-900 sm:pl-6"
						>Bidder rating</th
					>
					<th scope="col" class="px-3 py-3.5 pl-5 text-left text-sm font-semibold text-gray-900"
						>Completion time</th
					>
					<th scope="col" class="px-3 py-3.5 pl-5 text-left text-sm font-semibold text-gray-900"
						>Past jobs</th
					>
					<th scope="col" class="px-3 py-3.5 pl-5 text-left text-sm font-semibold text-gray-900"
						>Location</th
					>
				</tr>
			</thead>
			<tbody class="divide-y divide-gray-200 bg-white">
				{#each data.data as auction}
					<BidsTableSingleItem data={auction} />
				{/each}

				<!-- More people... -->
			</tbody>
		</table>
	</div>
</div>

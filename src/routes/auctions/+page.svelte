<script>
	export const ssr = true;
	import ItemBox from '../../components/itemBox.svelte';
	import { onMount } from 'svelte';
	import { isAuthenticated } from '$lib/auth';
	import { redirect } from '@sveltejs/kit';
	import { goto } from '$app/navigation';

	let loggedIn = false;
	onMount(async () => {
		loggedIn = await isAuthenticated();
		if (!loggedIn) {
			goto('/auth/login');
			//location.reload();
		}
	});
	export let data;
</script>

<div class="p-4 sm:ml-64">
	<div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700">
		{#if loggedIn}
			<ItemBox data={data.items} />
		{/if}
	</div>
</div>

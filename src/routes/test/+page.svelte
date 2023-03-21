<!-- This example requires Tailwind CSS v2.0+ -->
<script>
	import { goto } from '$app/navigation';
	import UserAuctionsList from '../../components/userAuctionsList.svelte';

	function handleNewAuction() {
		goto('/auctions/new');
	}

	export let data;
</script>

<UserAuctionsList {data} />

<script>
	import AuctionList from '../../components/auctionList.svelte';
	import { userSession } from '../../stores/userSession.js';

	/*
	let loggedIn = false;
	onMount(async () => {
		loggedIn = await isAuthenticated();
		if (!loggedIn) {
			console.log('Layout logged in: ' + loggedIn);
		}
	});
	loggedIn = loggedIn;
	*/
	/*
	let loggedIn = $userSession;
	loggedIn = loggedIn;
	console.log('test page logged in: ' + loggedIn);
	userSession.subscribe((value) => {
		loggedIn = value;
	});
	*/

	export let data;
</script>

<AuctionList {data} />

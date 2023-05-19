<script>
	import AuctionList from '../../components/auctionList.svelte';
	import { userSession } from '../../stores/userSession.js';
	import { documentUpload } from '../../stores/documentUpload';
	import { supabase } from '$lib/supabaseClient';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import ModalUploadDocumentError from '../../components/modalUploadDocumentError.svelte';

	let showModal = false;
	let documentUrl;

	onMount(async () => {
		await documentUpload.init();
		documentUpload.subscribe((value) => {
			//console.log('documentUploadStore changed:', value);
			documentUrl = value;
			checkAndRedirect();
		});
	});

	function checkAndRedirect() {
		if (documentUrl === null) {
			//console.log('User does not have a photo. Redirecting...');
			// Perform the redirection here
			showModal = true;
		} else {
			console.log('User has a photo.');
		}
	}

	export let data;
</script>

{#if showModal}
	<ModalUploadDocumentError />
{/if}

<AuctionList {data} />

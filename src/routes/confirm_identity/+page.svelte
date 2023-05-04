<script>
	import { userSession } from '../../stores/userSession.js';
	import { documentUpload } from '../../stores/documentUpload';
	import { supabase } from '$lib/supabaseClient';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { browser } from '$app/environment';

	let currentUser = $userSession;
	userSession.subscribe((value) => {
		if (browser) currentUser = value.user.id;
	});

	let photo_data = null;

	async function confirmIdentity() {
		//console.log('photo_data', photo_data);
		const response = await fetch('http://127.0.0.1:8000/confirm_identity', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			// body is data to json
			body: JSON.stringify({ photoURL: photo_data })
		});

		if (response.ok) {
			const result = await response.json();
			//const winner = result.winner;
			console.log('result received in svelte: ', JSON.stringify(result));
		} else {
			console.error('Error calculating winner:', response.status, response.statusText);
		}
	}

	onMount(() => {});

	async function getUserProfilePhoto(userId) {
		const folderPath = `profile-photos/${userId}/`;
		const { data: contents, error } = await supabase.storage.from('user-photos').list(folderPath);

		if (error) {
			console.error('Error fetching profile photo:', error);
			return null;
		}

		if (contents && contents.length > 0) {
			const validFile = contents.find((file) => file.name !== '.emptyFolderPlaceholder');
			if (validFile) {
				const fileUrl = `https://yqyheutdblzkrxymbhpw.supabase.co/storage/v1/object/public/user-photos/${folderPath}${validFile.name}`;
				return { photoURL: fileUrl, lastModified: validFile.metadata.lastModified };
			}
		}

		return null;
	}

	getUserProfilePhoto(currentUser).then((result) => {
		if (result && result.photoURL) {
			photo_data = result.photoURL;
			confirmIdentity();
		} else {
			console.log('User does not have a profile photo.');
		}
	});
</script>

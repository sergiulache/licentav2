<script>
	import { userSession } from '../../stores/userSession.js';
	import { documentUpload } from '../../stores/documentUpload';
	import { supabase } from '$lib/supabaseClient';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { browser } from '$app/environment';

	let video;

	let currentUser = $userSession;
	userSession.subscribe((value) => {
		if (browser) currentUser = value.user.id;
	});

	let photo_data = null;

	async function confirmIdentity() {
		//console.log('selfie data', capturedSelfie);
		const response = await fetch('http://127.0.0.1:8000/confirm_identity', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			// body is data to json
			body: JSON.stringify({ photoURL: photo_data, selfieDataUrl: capturedSelfie })
		});

		if (response.ok) {
			const result = await response.json();
			//const winner = result.winner;
			console.log('result received in svelte: ', JSON.stringify(result));
		} else {
			console.error('Error calculating winner:', response.status, response.statusText);
		}
	}

	onMount(async () => {
		if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
			try {
				const stream = await navigator.mediaDevices.getUserMedia({ video: true });
				video.srcObject = stream;
			} catch (error) {
				console.error('Error accessing the webcam:', error);
			}
		} else {
			console.error('getUserMedia not supported in this browser.');
		}
	});

	let capturedSelfie = '';
	function capture() {
		const context = canvas.getContext('2d');
		context.drawImage(video, 0, 0, 640, 480);
		const dataUrl = canvas.toDataURL('image/jpeg');
		capturedSelfie = dataUrl;
		console.log('photoURL', photo_data);
		confirmIdentity();
	}

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
		if (browser) {
			if (result && result.photoURL) {
				photo_data = result.photoURL;
			} else {
				console.log('User does not have a profile photo.');
			}
		}
	});
</script>

<div class="space-y-6 p-4 sm:ml-64">
	<div class="bg-white shadow px-4 py-5 sm:rounded-lg sm:p-6">
		<video bind:this={video} width="640" height="480" autoplay />
		<button
			on:click={capture}
			type="button"
			class="mt-6 w-full p-4 rounded-md border border-gray-300bg-white text-base font-medium text-gray-700 shadow-sm hover:bg-green-50 hover:ring-green-500 hover:ring-offset-2  hover:ring-2 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:w-auto sm:text-sm"
			>Capture Selfie</button
		>
		<canvas id="canvas" width="640" height="480" style="display:none;" />
	</div>
</div>

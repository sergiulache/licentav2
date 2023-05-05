<script>
	import { userSession } from '../../stores/userSession.js';
	import { documentUpload } from '../../stores/documentUpload';
	import { supabase } from '$lib/supabaseClient';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { browser } from '$app/environment';
	import AlertFaceVerificationSuccess from '../../components/alertFaceVerificationSuccess.svelte';

	let video;
	let showAlert = false;

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
			showAlert = true;
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

{#if showAlert}
	<AlertFaceVerificationSuccess />
{/if}

<div class="space-y-6 p-4 sm:ml-64">
	<div class="bg-white box-shadow-xl px-4 py-5 sm:rounded-lg sm:p-6">
		<canvas id="canvas" width="640" height="480" style="display:none;" />
		<div class="relative bg-white py-2 sm:py-2">
			<div class="lg:mx-auto lg:max-w-7xl lg:px-8 lg:grid lg:grid-cols-2 lg:gap-24 lg:items-start">
				<div class="relative sm:py-16 lg:py-0">
					<div
						aria-hidden="true"
						class="hidden sm:block lg:absolute lg:inset-y-0 lg:right-0 lg:w-screen"
					>
						<div class="absolute inset-y-0 right-1/2 w-full bg-gray-50 rounded-r-3xl lg:right-72" />
					</div>
					<div
						class="relative mx-auto max-w-md px-4 sm:max-w-3xl sm:px-6 lg:px-0 lg:max-w-none lg:py-20 "
					>
						<!-- Testimonial card-->
						<div class="relative pt-64 pb-10 rounded-2xl shadow-xl overflow-hidden">
							<video
								bind:this={video}
								width="640"
								height="480"
								autoplay
								class="rounded-3xl drop-shadow-2xl border-gray-500 absolute inset-0 h-full w-full object-cover"
							>
								<track kind="captions" />
							</video>
						</div>
						<div class="flex items-center justify-center">
							<button
								on:click={capture}
								type="button"
								class="w-1/3 py-3 mt-8 px-8 flex items-center justify-center text-base bg-indigo-500 text-white hover:bg-indigo-700 hover:-translate-y-1 hover:scale-105 hover:border-indigo-400 border-b-4 rounded-lg duration-300"
								>Capture Selfie</button
							>
						</div>
					</div>
				</div>

				<div class="relative mx-auto max-w-md px-4 sm:max-w-3xl sm:px-6 lg:px-0">
					<!-- Content area -->
					<div class="pt-12 sm:pt-16 lg:pt-20">
						<h2 class="text-3xl text-gray-900 font-extrabold tracking-tight sm:text-4xl">
							Verification photo
						</h2>
						<div class="mt-6 text-gray-500 space-y-6">
							<p class="text-lg">
								Please take a selfie with your webcam. This will be used to verify your identity
								with the document you have uploaded previously. Please make sure your face is
								clearly visible, and that there is good lighting.
							</p>
							<p class="text-base leading-7">
								By proceeding with the selfie capture, you consent to the use of your photo for the
								sole purpose of verifying your identity against the previously uploaded document.
								Your photo will be processed with utmost respect for your privacy, and it will not
								be used for any other purposes or shared with third parties. By continuing, you
								agree to these terms.
							</p>
							<p class="text-base leading-7 text-green-800">
								Your photo will be deleted from our servers after the verification process.
							</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>

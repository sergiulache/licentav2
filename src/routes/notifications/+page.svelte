<script>
	import { onMount } from 'svelte';
	import { supabase } from '$lib/supabaseClient';
	import { goto } from '$app/navigation';

	import { browser } from '$app/environment';
	import { get } from 'svelte/store';
	import toast, { Toaster } from 'svelte-french-toast';

	export let data;

	//console.log(data.props.notifications);

	let notifications = data.props.notifications.map((notification) => {
		return {
			...notification,
			title: `Notification for item ${notification.item_title}`, // modify this line to suit your title requirements
			body: `You have won the auction ${notification.item_title}.` // modify this line to suit your body requirements
		};
	});

	async function dismissNotification(notification) {
		notification.dismissed = true;
		const { data, error } = await supabase
			.from('notifications')
			.update({ dismissed: true })
			.eq('id', notification.notification_id);

		if (error) {
			console.error('Error updating notification: ', error);
			// revert the dismissed state if there was an error
			notification.dismissed = false;
		} else {
			notifications = notifications.map((n) =>
				n.notification_id === notification.notification_id ? notification : n
			);
		}
	}
</script>

<div class="space-y-6 p-4 sm:ml-64">
	<div class="bg-white box-shadow-xl px-4 py-5 sm:rounded-lg sm:p-6">
		<div>
			<div class="flow-root mt-6">
				<ul class="-my-5 divide-y divide-gray-200">
					{#if notifications}
						{#each notifications as notification (notification.notification_id)}
							<li class="py-5">
								<div
									class={notification.dismissed
										? 'relative bg-gray-300 rounded-lg p-3 flex justify-between items-start dismissed'
										: 'relative bg-green-600/25 rounded-lg p-3 flex justify-between items-start'}
								>
									<div>
										<h3 class="text-sm font-semibold text-gray-800">
											{notification.title}
										</h3>
										<p class="mt-1 text-sm text-gray-600 line-clamp-2">{notification.body}</p>
									</div>
									<button
										class="rounded-md border border-light-blue-300 text-light-blue-500 px-3 py-1 float-right"
										on:click={() => dismissNotification(notification)}
									>
										Dismiss
									</button>
								</div>
							</li>
						{/each}
					{/if}
				</ul>
			</div>
			<div class="mt-6">
				<a
					href="/notifications"
					class="w-full flex justify-center items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
				>
					View all
				</a>
			</div>
		</div>
	</div>
</div>

<style>
	.dismissed {
		background-color: rgba(209, 213, 219, 0.5);
		color: black;
	}
</style>

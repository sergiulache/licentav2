<script>
	import { current } from '../stores/currentNav';

	function handleClick(path) {
		$current = path;
	}
</script>

<div>
	<li
		class="hover:-translate-y-1 hover:scale-105 hover:border-indigo-400 border-b-2 rounded-lg duration-300"
	>
		<a
			href="/profile"
			class:active={$current === '/profile'}
			on:click={() => handleClick('/profile')}
			class="flex items-center p-2 pr-28 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
		>
			<i class="fa-solid fa-address-card fa-lg text-gray-600" />
			<span class="ml-3 text-gray-600">My profile</span>
		</a>
	</li>
</div>

<style>
	.active {
		background-color: #ff3e00;
		color: white;
	}
</style>

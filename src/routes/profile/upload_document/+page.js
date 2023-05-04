import { supabase } from '$lib/supabaseClient';
import { redirect } from '@sveltejs/kit';
import { isAuthenticated } from '$lib/auth';
import { userSession } from '../../../stores/userSession';
import { getCurrentUserID } from '$lib/auth';
import { get } from 'svelte/store';
import { browser } from '$app/environment';

export async function load() {}

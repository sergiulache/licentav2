import { supabase } from '../lib/supabaseClient';
import { writable } from 'svelte/store';
import { browser } from '$app/environment';
import { getCurrentUserID } from '$lib/auth';

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

function createDocumentUploadStore() {
	const { subscribe, set, update } = writable(null);

	return {
		subscribe,
		set,
		update,
		init: async () => {
			const userID = await getCurrentUserID();
			const result = await getUserProfilePhoto(userID);

			if (result && result.photoURL) {
				set(result.photoURL);
			} else {
				set(null);
				console.log('User does not have a profile photo. (document store)');
			}
		}
	};
}

export const documentUpload = createDocumentUploadStore();

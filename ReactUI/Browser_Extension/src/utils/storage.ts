export const storage = {
  get: (key: string): Promise<any> => {
    return new Promise((resolve) => {
      if (
        typeof chrome !== "undefined" &&
        chrome.storage
      ) {
        chrome.storage.local.get(
          [key],
          (result) => {
            resolve(result[key]);
          }
        );
      } else {
        // DEV fallback
        resolve(localStorage.getItem(key));
      }
    });
  },

  set: (key: string, value: any) => {
    if (
      typeof chrome !== "undefined" &&
      chrome.storage
    ) {
      chrome.storage.local.set({
        [key]: value,
      });
    } else {
      localStorage.setItem(key, value);
    }
  },

  remove: (key: string) => {
    if (
      typeof chrome !== "undefined" &&
      chrome.storage
    ) {
      chrome.storage.local.remove(key);
    } else {
      localStorage.removeItem(key);
    }
  },
};

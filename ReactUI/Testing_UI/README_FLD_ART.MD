Browser_Extension/
│
├── public/
│   ├── manifest.json
│   ├── background.js
│   └── icons/
│
├── src/
│
│   ├── api/
│   │   └── apiClient.ts
│
│   ├── components/
│   │
│   │   ├── auth/
│   │   │   └── LoginPage.tsx
│   │   │
│   │   ├── chat/
│   │   │   ├── ChatPage.tsx
│   │   │   ├── ChatInput.tsx
│   │   │   ├── ChatMessages.tsx
│   │   │   └── UploadModal.tsx
│   │   │
│   │   ├── common/
│   │   │   └── Toast.tsx
│   │
│   ├── hooks/
│   │   └── useAuth.ts
│   │
│   ├── models/
│   │   └── ChatTypes.ts
│   │
│   ├── styles/
│   │   ├── global.css
│   │   ├── chat.css
│   │   ├── upload.css
│   │   └── auth.css
│   │
│   ├── utils/
│   │   └── storage.ts
│   │
│   ├── App.tsx
│   ├── popup.tsx
│   └── main.tsx
│
├── .env
├── .env.development
├── .env.production
│
├── tsconfig.json
├── vite.config.ts
└── package.json





styles/
│
├── base.css
├── layout.css
├── chat.css
├── login.css
├── upload.css
├── toast.css
└── popup.css (main importer)

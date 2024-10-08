// app/layout.tsx
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Script from "next/script"; // Import Script component
import "./globals.css";
import { Header } from "./ui/header";
import { Footer } from "./ui/footer";
import { AuthUserProvider } from "@/app/context/authContext";
import BrevoWidget from "@/app/components/BrevoWidget";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "ACME Education",
  description:
    "An e-platform that aims to make the learning process easier for all involved.",
};

const googleTagId = process.env.NEXT_PUBLIC_GOOGLE_TAG_ID;

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{metadata.title as string}</title>
        <meta name="description" content={metadata.description as string} />

        {/* Google tag (gtag.js) */}
        <Script
          strategy="afterInteractive"
          src={`https://www.googletagmanager.com/gtag/js?id=${googleTagId}`}
        />
        <Script id="google-analytics" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', '${googleTagId}');
          `}
        </Script>
      </head>
      <body className={inter.className}>
        <AuthUserProvider>
          <Header />
          {children}
          <Footer />
          <BrevoWidget />
        </AuthUserProvider>
      </body>
    </html>
  );
}


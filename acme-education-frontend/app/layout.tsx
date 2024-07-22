// app/layout.tsx
import type { Metadata } from "next";
import { Inter } from "next/font/google";
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



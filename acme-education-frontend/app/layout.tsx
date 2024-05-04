import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Header } from "./ui/header";
import { Footer } from "./ui/footer";
import { AuthUserProvider } from "@/app/context/authContext";

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
      <body className={inter.className}>
        <AuthUserProvider>
          <Header />
          {children}
          <Footer />
        </AuthUserProvider>
      </body>
    </html>
  );
}

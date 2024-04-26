// import Login from "../components/Login";

import { SignInForm } from "../components/form";

export default async function Page({
  params,
}: {
  params: { product: string };
}) {
  return <SignInForm />;
}

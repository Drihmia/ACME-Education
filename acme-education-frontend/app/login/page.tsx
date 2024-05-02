import { SignInForm } from "../ui/form";

export default async function Page({
  params,
}: {
  params: { product: string };
}) {
  return <SignInForm />;
}

"use client";

import { useAuth } from "@/app/context/authContext";
import { ProfileSkeleton } from "@/app/ui/skeletons";
import { Profile } from "@/app/ui/dashboard/profile";
import { Suspense } from "react";
import { useRouter } from "next/navigation";

export default function Page() {
  const { user } = useAuth()!;
  const router = useRouter()

  if (!user) return router.push("/login")

  return (
    <Suspense fallback={<ProfileSkeleton />}>
      <Profile user={user} />
    </Suspense>
  );
}

"use client";

import { useAuth } from "@/app/context/authContext";
import { ProfileSkeleton } from "@/app/ui/skeletons";
import { Profile } from "@/app/ui/dashboard/profile";
import { Suspense } from "react";
import { useRouter } from "next/navigation";
import { UpdateProfileModal } from "@/app/ui/dashboard/modals/updateProfileModal";
import { ProfileModalWrapper } from "@/app/ui/modalWrapper";

export default function Page() {
  const { user } = useAuth()!;
  const router = useRouter()

  if (!user) return router.push("/login")

  return (
    <Suspense fallback={<ProfileSkeleton />}>
      <ProfileModalWrapper ProfileComponent={Profile} Modal={UpdateProfileModal} user={user} />
    </Suspense>
  );
}

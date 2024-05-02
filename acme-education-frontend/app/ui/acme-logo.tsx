import { Icon } from "@iconify/react/dist/iconify.js";


export default function AcmeLogo() {
  return (
    <div
      className={`flex flex-row items-center leading-none text-white`}
    >
      <Icon icon="zondicons:education" />
      <p className="text-[44px]">ACME</p>
    </div>
  );
}

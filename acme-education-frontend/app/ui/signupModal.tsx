import { Icon } from "@iconify/react/dist/iconify.js";
import { useRouter } from "next/navigation";

export const SignUpModal = ({
  closeModal,
  response,
}: {
  closeModal: () => void;
  response: {status: string, message: string};
}) => {
    const navigation = useRouter()
  return (
    <div className="fixed top-0 left-0 w-screen h-screen flex items-center justify-center bg-black/25">
      <div className="relative w-full max-w-md h-48 p-4 md:p-8 flex flex-col justify-between gap-8 rounded-md bg-white">
        <div className="w-full">
          {response.status == "success" ? (
            <>
            <h2 className="flex items-center gap-2 text-xl md:text-2xl font-bold text-green-700">
            <Icon color="green" icon="mdi:success-bold" />
            Verification email sent!
          </h2>
              <p className="text-gray-600">
            Check your inbox to complete your registration.
          </p>
            </>
          ) : (
            <>
            <h2 className="flex items-center gap-2 text-xl md:text-2xl font-bold text-red-500">
            <Icon icon="pajamas:error" />
              Oops
            </h2>
            <p>{response.message}</p>
            </>
          )}
        </div>
        {response.status == "success" ?
        <div onClick={() => navigation.push('/')} className="min-w-24 h-8 self-end flex items-center justify-center p-2 bg-blue-200 hover:bg-blue-700 cursor-pointer rounded-md hover:text-white">
          Ok
        </div> :
        <button onClick={closeModal} className="min-w-24 h-8 self-end flex items-center justify-center p-2 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white">
          Try again
        </button>}
      </div>
    </div>
  );
};

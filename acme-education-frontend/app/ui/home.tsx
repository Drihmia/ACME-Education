import Link from "next/link";

export const HomePage = () => {
  return (
    <main className="w-full">
      <div className="w-full h-[calc(100vh-64px)] md:h-[calc(100vh-80px)] flex flex-col gap-4 items-center justify-center bg-landing bg-center bg-no-repeat bg-cover">
        <div className="w-full max-w-3xl grid gap-4 text-center">
          <h1 className="text-3xl md:text-4xl lg:text-5xl font-bold text-center text-black">
            Connect, Learn, and Grow: The Ultimate Platform for Teachers and
            Students
          </h1>
          <p className="text-xl md:text-2xl font-medium">
            Welcome to the ultimate educational platform where diversity meets
            simplicity. Our innovative system is designed to cater to the
            dynamic needs of modern educators and students alike.
          </p>
          <Link
            href={"/signup"}
            className="w-96 mx-auto bg-blue-500 text-white hover:bg-black font-bold p-2 md:p-4 rounded-xl mt-4"
          >
            Sign Up To Start Sharing Knowledge Today
          </Link>
        </div>
      </div>
      <div className="w-full p-4 md:p-8 lg:p-16 xl:p-24 grid bg-black text-slate-50">
        <div className="w-full text-center">
          <h2 className="text-xl md:text-3xl font-bold mb-2">
            Empower Your Teaching with Flexibility and Reach
          </h2>
          <p className="font-medium">
            Here’s how we make teaching and learning more accessible and
            efficient
          </p>
        </div>
        <ul className="w-full flex flex-col items-center gap-4 md:grid md:grid-cols-2 md:gap-6 mt-4">
          <li className="w-full max-w-xl grid gap-2 md-gap-4 md:p-4 mb-2">
            <span className="w-full flex item-center justify-center font-bold text-xl md:text-2xl text-white">
              Multi-Subject Publishing
            </span>
            <span className="w-full max-w-md mx-auto text-center">
              Teachers are not limited to one field. Share your knowledge across
              various subjects within your expertise.
            </span>
          </li>
          <li className="w-full max-w-xl grid gap-2 md-gap-4 md:p-4 mb-2">
            <span className="w-full flex item-center justify-center font-bold text-xl md:text-2xl text-white">
              Institutional Versatility
            </span>
            <span className="w-full max-w-md mx-auto text-center">
              Whether you’re affiliated with one or multiple institutions, our
              platform enables you to disseminate your lessons to all of them
              seamlessly.
            </span>
          </li>
          <li className="w-full max-w-xl grid gap-2 md-gap-4 md:p-4 mb-2">
            <span className="w-full flex item-center justify-center font-bold text-xl md:text-2xl text-white">
              Class Customization
            </span>
            <span className="w-full max-w-md mx-auto text-center">
              Tailor your teaching to specific classes. Choose to engage with
              all or select few, depending on your teaching strategy.
            </span>
          </li>
          <li className="w-full max-w-xl grid gap-2 md-gap-4 md:p-4 mb-2">
            <span className="w-full flex item-center justify-center font-bold text-xl md:text-2xl text-white">
              Simplified Lesson Management
            </span>
            <span className="w-full max-w-md mx-auto text-center">
              Say goodbye to the hassle of multiple lesson versions. Publish
              once, edit anytime, and update everywhere with ease.
            </span>
          </li>
          <li className="w-full max-w-xl grid gap-2 md-gap-4 md:p-4">
            <span className="w-full flex item-center justify-center font-bold text-xl md:text-2xl text-white">
              Unified Lesson Experience
            </span>
            <span className="w-full max-w-md mx-auto text-center">
              Students from different institutions but the same class can access
              the same lesson content, ensuring a standardized learning
              experience.
            </span>
          </li>
        </ul>
        {/* <div className="mt-8 text-center mb-8">
          <p className="font-medium">
            Join us and transform the way you teach and reach students. Because
            when it comes to education, we believe in breaking barriers, not
            creating them.
          </p>
          <button className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded mt-4">
            Start Sharing Knowledge Today
          </button>
        </div> */}
      </div>
      <div className="w-full p-4 md:p-8 lg:p-16 xl:p-24 bg-sky-50">
        <h2 className="text-center text-xl md:text-3xl font-bold mb-2">
          Evolving Education: What’s Next for Our Platform
        </h2>
        <p className="text-center font-medium">
          Our commitment to providing a top-notch educational experience drives
          us to constantly innovate. Here’s a glimpse into the future
          enhancements we’re excited to bring to our platform
        </p>
        <ul className="w-full grid gap-4 py-4 md:py-8 mt-4">
          <li>
            <span className="font-medium">Interactive Feedback:</span> A new feedback button/form will allow students
            to rate lessons and share their opinions, fostering a
            community-driven quality assurance system.
          </li>
          <li>
            <span className="font-medium">Engaged Learning Community:</span> A comment section on each lesson will
            enable students to ask questions and receive answers from peers or
            teachers, enhancing collaborative learning.
          </li>
          <li>
            <span className="font-medium">Exclusive Group Chats:</span> We’re set to activate private group chats,
            creating dedicated spaces for teachers and their students to
            discuss, collaborate, and grow together.
          </li>
          <li>
            <span className="font-medium">Security at the Forefront:</span> Our existing email verification system
            ensures every account is genuine, maintaining a secure environment
            and peace of mind for all users.
          </li>
        </ul>
      <div className="text-center">
        <p className="text-gray-700">
          Stay tuned as we continue to shape the future of education, one
          feature at a time.
        </p>
        <button className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded mt-4">
          Discover More
        </button>
      </div>
      </div>
    </main>
  );
};

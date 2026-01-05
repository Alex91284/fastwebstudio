import { Link } from "react-router-dom"

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen text-center bg-gray-100">
      <h1 className="text-6xl font-bold text-red-600">404</h1>
      <h2 className="mt-4 text-2xl font-semibold">Página no encontrada</h2>
      <p className="mt-2 text-gray-600">
        Lo sentimos, la página que buscas no existe.
      </p>
      <Link
        to="/"
        className="px-4 py-2 mt-6 text-white transition bg-blue-600 rounded hover:bg-blue-700"
      >
        Volver al inicio
      </Link>
    </div>
  )
}

def get_navbar():
    return """
    <nav class="bg-blue-500 p-4">
        <div class="container mx-auto">
            <div class="flex items-center justify-between">
                <div class="text-white text-lg font-bold">My Website</div>
                <div>
                    <a href="/" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Home</a>
                    <a href="/hello/" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Hello</a>
                    <a href="/signup/" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Signup</a>
                    <a href="/login/" class="text-gray-300 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Login</a>
                </div>
            </div>
        </div>
    </nav>
    """

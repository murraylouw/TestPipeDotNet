using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Pipes;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace TestPipeDotNet
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Start this program first, then run the Python project: TestPipePython
            // Based on example from: https://jonathonreinhart.com/posts/blog/2012/12/13/named-pipes-between-c-and-python/

            // Open the named pipe.
            var server = new NamedPipeServerStream("ik_pipe");

            Console.WriteLine("Waiting for connection...");
            server.WaitForConnection();
            Console.WriteLine("Connected.");

            var reader = new BinaryReader(server);
            var writer = new BinaryWriter(server);

            while (true)
            {
                try
                {
                    // Send input data
                    string tcp_pose = " 0.5     1.0     1.5     10      20      30 ";
                    string message_from_dotnet = string.Format("<tcp_pose>{0}<tcp_pose/>", tcp_pose);

                    var buffer = Encoding.ASCII.GetBytes(message_from_dotnet);     // Get ASCII byte array     
                    writer.Write((uint)buffer.Length);                // Write string length
                    writer.Write(buffer);                              // Write string
                    Console.WriteLine("Sent from .NET: \"{0}\"", message_from_dotnet);


                    // Receive output data
                    var received_str_length = (int)reader.ReadUInt32();            // Read string length
                    var received_string = new string(reader.ReadChars(received_str_length));    // Read string

                    Console.WriteLine("Received from Python: \"{0}\"", received_string);
                    Console.WriteLine();

                    Thread.Sleep(2000); // Wait for 2 seconds
                    
                }
                catch (EndOfStreamException) // When client disconnects
                {
                    Console.WriteLine("Client disconnected.");
                    break;                    
                }
            }
            
            server.Close();
            server.Dispose();
        }
    }
}

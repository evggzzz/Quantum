namespace HelloWorld
{
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Primitive;

    namespace HelloWorld
    {
        open Microsoft.Quantum.Intrinsic;
        open Microsoft.Quantum.Canon;

        operation SayHello() : Result {
            Message("Hello from quantum world!");
            return Zero;
        }
    }

    operation Set (desired: Result, q1: Qubit) : Unit {
        let current = M(q1);
        if (desired != current)
        {
            X(q1);
        }
    }

    operation SetTest (count : Int, initial: Result) : (Int,Int) {
        mutable numOnes = 0;
        using (qubit = Qubit())
        {
            for (test in 1 .. count)
            {
                Set (initial, qubit);

                let res = M(qubit);

                //count the number of ones we saw:
                if (res == One)
                {
                    set numOnes = numOnes + 1;
                }
            }
            Reset(qubit);
        }
        // Return number of times we saw a |0> and number of times we saw a |1>
        return (count - numOnes, numOnes);
    }
}

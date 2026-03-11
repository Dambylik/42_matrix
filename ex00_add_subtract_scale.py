from linear_algebra import Vector, Matrix

def main():
    v_1 = Vector([2.0, 3.0])
    v_2 = Vector([5.0, 7.0])

    m_1 = Matrix([[1.0, 2.0],
                  [3.0, 4.0]])
    m_2 = Matrix([[7.0, 4.0],
                  [-2.0, 2.0]])
    a = 2.0
    
    print ("Added vector :", v_1.add(v_2))
    #print ("Substracted vector :", v_1.sub(v_2))
    #print ("Scaled vector :", v_1.scl(a))
    print ("-" * 50)
    #print ("Added matrix :", m_1.add(m_2))
    #print ("Substracted matrix :", m_1.sub(m_2))
    #print ("Scaled matrix :", m_1.scl(a))
    return


if __name__ == '__main__':
    main()




# encoding: utf-8

# global variable
x = ''

with context('before after hooks'):
    with before.all:
        print 'This code will be run once, before all examples'

    with before.each:
        print 'This code will be run before each example'

    with it('sample 1'):
        pass

    with it('sample 2'):
        pass

    with context('sub-context'):
        with before.each:
            print 'set value in the before phrase'
            x = 'before sub context'
            self.x = 'self variable before sub context'

        with it('print x'):
            print 'scope is different :%s, %s' % (x, self.x)

    with after.each:
        # this timing seems strange.
        print 'This code will be run after each example'

    with after.all:
        print 'This code will be run once, after all examples'
